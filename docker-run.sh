docker build --tag dummy .
docker run -v $PWD:/workspace -p 8080:8080 dummy