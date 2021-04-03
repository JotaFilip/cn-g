
printf "Installing proto dependencies . . ."
     sudo apt update
     sudo apt install python3
     sudo apt-get -y install python3-pip
     pip3 install --upgrade pip
     python3 -m pip install --upgrade testresources
     python3 -m pip install --upgrade setuptools
     pip3 install --no-cache-dir --force-reinstall -Iv grpcio
     pip3 install grpcio-tools
     pip3 install grpc-interceptor
     pip3 install --upgrade protobuf
     pip3 install wheel


printf " done\n"