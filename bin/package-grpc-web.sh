rm -rf grpc-web-artifacts
mkdir grpc-web-artifacts
cp package.json grpc-web-artifacts/
cp publish.json grpc-web-artifacts/
cp -f ../protobuf/gen/pb-web/* ./grpc-web-artifacts/
cd grpc-web-artifacts
npm pack
