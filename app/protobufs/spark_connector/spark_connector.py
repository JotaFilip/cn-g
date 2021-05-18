from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from spark_connector_pb2 import *
import spark_connector_pb2_grpc
from utils_pb2 import *

import re

from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage

project_id = "cn-g14-projecto"
region = "europe-west4"
cluster_name = "cluster-spark"

def submit_job(project_id, region, job):
    # Create the job client.
    job_client = dataproc.JobControllerClient(client_options={
        'api_endpoint': '{}-dataproc.googleapis.com:443'.format(region)
    })

    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job}
    )
    response = operation.result()

    # Dataproc job output gets saved to the Google Cloud Storage bucket
    # allocated to the job. Use a regex to obtain the bucket and blob info.
    matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)

    output = (
        storage.Client()
            .get_bucket(matches.group(1))
            .blob(f"{matches.group(2)}.000000000")
            .download_as_string()
    )

    return output

class Spark_Connector(spark_connector_pb2_grpc.Spark_ConnectorServicer):

    def GetPersonWhoWorkedWithMorePeopleToSameMovie(self, request, context):
        job = {
            'placement': {
                'cluster_name': cluster_name
            },
            "sparkJob": {
                "mainJarFileUri": "gs://cn-spark-bucket/mygraphoperations_2.12-0.1.0.jar",
                "properties": {}
            }
        }
        output = submit_job(project_id, region, job)
        return ExecutionResult(output=output)
    def GetBestDirector(self, request, context):
        job = {
            'placement': {
                'cluster_name': cluster_name
            },
            "pysparkJob": {
                "mainPythonFileUri": "gs://cn-spark-bucket/query2.py",
                "properties": {}
            }
        }
        output = submit_job(project_id, region, job)

        return ExecutionResult(output=output)

    # def GetDirectorWork(self,request,context):
    #     # TODO
    #     out = execute_job(request, context)
    #     return ExecutionResult(output = out)
    #
    # def GetFamousActor(self,request,context):
    #     # TODO
    #     out = execute_job(request, context)
    #     return ExecutionResult(output=out)
    #
    # def execute_job(self,request,context):
    #     project_id = "cn-g14-projeto"
    #     zone = "europe-west4"
    #     cluster_name = "cluster-spark"
    #     bucket_name = "cn-spark-bucket"
    #     # Which file is executed can be defined by the type of request that is sent
    #     pyspark_file = ""
    #     create_new_cluster = False
    #
    #     # [START dataproc_get_client]
    #     if global_region:
    #         region = "global"
    #         # Use the default gRPC global endpoints.
    #         dataproc_cluster_client = dataproc_v1.ClusterControllerClient()
    #         dataproc_job_client = dataproc_v1.JobControllerClient()
    #     else:
    #         region = get_region_from_zone(zone)
    #         # Use a regional gRPC endpoint. See:
    #         # https://cloud.google.com/dataproc/docs/concepts/regional-endpoints
    #         client_transport = cluster_controller_grpc_transport.ClusterControllerGrpcTransport(
    #             address="{}-dataproc.googleapis.com:443".format(region)
    #         )
    #         job_transport = job_controller_grpc_transport.JobControllerGrpcTransport(
    #             address="{}-dataproc.googleapis.com:443".format(region)
    #         )
    #         dataproc_cluster_client = dataproc_v1.ClusterControllerClient(client_transport)
    #         dataproc_job_client = dataproc_v1.JobControllerClient(job_transport)
    #     # [END dataproc_get_client]
    #
    #     try:
    #         spark_file, spark_filename = get_pyspark_file(pyspark_file)
    #         if create_new_cluster:
    #             create_cluster(
    #                 dataproc_cluster_client, project_id, zone, region, cluster_name
    #             )
    #             wait_for_cluster_creation()
    #         upload_pyspark_file(project_id, bucket_name, spark_filename, spark_file)
    #
    #         list_clusters_with_details(dataproc_cluster_client, project_id, region)
    #
    #         (cluster_id, output_bucket) = get_cluster_id_by_name(
    #             dataproc_cluster_client, project_id, region, cluster_name
    #         )
    #
    #         # [START dataproc_call_submit_pyspark_job]
    #         job_id = submit_pyspark_job(
    #             dataproc_job_client,
    #             project_id,
    #             region,
    #             cluster_name,
    #             bucket_name,
    #             spark_filename,
    #         )
    #         # [END dataproc_call_submit_pyspark_job]
    #
    #         wait_for_job(dataproc_job_client, project_id, region, job_id)
    #         output = download_output(project_id, cluster_id, output_bucket, job_id)
    #         print("Received job output {}".format(output))
    #         return output
    #     finally:
    #         if create_new_cluster:
    #             delete_cluster(dataproc_cluster_client, project_id, region, cluster_name)
    #             spark_file.close()

    # def get_pyspark_file(pyspark_file=None):
    #     if pyspark_file:
    #         f = open(pyspark_file, "rb")
    #         return f, os.path.basename(pyspark_file)
    #     else:
    #         """Gets the PySpark file from current directory."""
    #         current_dir = os.path.dirname(os.path.abspath(__file__))
    #         f = open(os.path.join(current_dir, DEFAULT_FILENAME), "rb")
    #         return f, DEFAULT_FILENAME

    # def get_region_from_zone(zone):
    #     try:
    #         region_as_list = zone.split("-")[:-1]
    #         return "-".join(region_as_list)
    #     except (AttributeError, IndexError, ValueError):
    #         raise ValueError("Invalid zone provided, please check your input.")
    #
    # def upload_pyspark_file(project, bucket_name, filename, spark_file):
    #     """Uploads the PySpark file in this directory to the configured input
    #     bucket."""
    #     print("Uploading pyspark file to Cloud Storage.")
    #     client = storage.Client(project=project)
    #     bucket = client.get_bucket(bucket_name)
    #     blob = bucket.blob(filename)
    #     blob.upload_from_file(spark_file)
    #
    # def download_output(project, cluster_id, output_bucket, job_id):
    #     """Downloads the output file from Cloud Storage and returns it as a
    #     string."""
    #     print("Downloading output file.")
    #     client = storage.Client(project=project)
    #     bucket = client.get_bucket(output_bucket)
    #     output_blob = "google-cloud-dataproc-metainfo/{}/jobs/{}/driveroutput.000000000".format(
    #         cluster_id, job_id
    #     )
    #     return bucket.blob(output_blob).download_as_string()
    #
    # # [START dataproc_list_clusters_with_detail]
    # def list_clusters_with_details(dataproc, project, region):
    #     """List the details of clusters in the region."""
    #     for cluster in dataproc.list_clusters(
    #             request={"project_id": project, "region": region}
    #     ):
    #         print(
    #             (
    #                 "{} - {}".format(
    #                     cluster.cluster_name,
    #                     cluster.status.State.Name(cluster.status.state),
    #                 )
    #             )
    #         )

    # [END dataproc_list_clusters_with_detail]

    # def get_cluster_id_by_name(dataproc, project_id, region, cluster_name):
    #     """Helper function to retrieve the ID and output bucket of a cluster by
    #     name."""
    #     for cluster in dataproc.list_clusters(
    #             request={"project_id": project_id, "region": region}
    #     ):
    #         if cluster.cluster_name == cluster_name:
    #             return cluster.cluster_uuid, cluster.config.config_bucket
    #
    # # [START dataproc_submit_pyspark_job]
    # def submit_pyspark_job(dataproc, project, region, cluster_name, bucket_name, filename):
    #     """Submit the Pyspark job to the cluster (assumes `filename` was uploaded
    #     to `bucket_name."""
    #     job_details = {
    #         "placement": {"cluster_name": cluster_name},
    #         "pyspark_job": {
    #             "main_python_file_uri": "gs://{}/{}".format(bucket_name, filename)
    #         },
    #     }
    #
    #     result = dataproc.submit_job(
    #         request={"project_id": project, "region": region, "job": job_details}
    #     )
    #     job_id = result.reference.job_id
    #     print("Submitted job ID {}.".format(job_id))
    #     return job_id

    # [END dataproc_submit_pyspark_job]

    # [START dataproc_wait]
    # def wait_for_job(dataproc, project, region, job_id):
    #     """Wait for job to complete or error out."""
    #     print("Waiting for job to finish...")
    #     while True:
    #         job = dataproc.get_job(
    #             request={"project_id": project, "region": region, "job_id": job_id}
    #         )
    #         # Handle exceptions
    #         if job.status.State.Name(job.status.state) == "ERROR":
    #             raise Exception(job.status.details)
    #         elif job.status.State.Name(job.status.state) == "DONE":
    #             print("Job finished.")
    #             return job

    # [END dataproc_wait]

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    spark_connector_pb2_grpc.add_Spark_ConnectorServicer_to_server(
        Spark_Connector(), server
    )
    
    server.add_insecure_port("[::]:50058")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()