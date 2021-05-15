package com.example
import org.apache.spark.sql._
import org.apache.spark.sql.functions._

import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark._
import org.apache.spark.graphx.GraphLoader
import scala.util.MurmurHash
import org.apache.spark.graphx.Graph
import org.apache.spark.rdd.RDD
import org.apache.spark.graphx.VertexId
import org.apache.spark.graphx._
// To make some of the examples work we will also need RDD
import org.apache.spark.rdd.RDD

object MyGraphOperations {
  def main(args: Array[String]) {
    val spark =
      SparkSession.builder.appName("MyFirstScalaSpark").getOrCreate()
    val e = spark.read
      // Adjust separator if needed
      .options(Map("header" -> "true"))
      .csv("gs://cn-spark-bucket/edges.csv")
    val v = spark.read
      // Adjust separator if needed
      .options(Map("header" -> "true"))
      .csv("gs://cn-spark-bucket/verts.csv")

    val users: RDD[(VertexId, String)] =
      v.rdd.distinct().map(p =>
        (MurmurHash.stringHash(p.toString), p.toString))
    val edgesRDD: RDD[Edge[String]] =
      e.rdd.map(r => {
        val p = Edge(MurmurHash.stringHash(r.getString(0)), MurmurHash.stringHash(r.getString(1)), "colega")
        p
      })

    val defaultUser = ("Missing")
    // Build the initial Graph
    val graph = Graph(users, edgesRDD, defaultUser)

    println("Result: " + graph.numVertices)
    spark.stop
  }
}
