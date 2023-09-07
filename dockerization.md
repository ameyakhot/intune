## build & run

// inside /src -> Here, mock.dockerfile is present

docker build -t backend-mock-msi -f mock.dockerfile .

docker run -d --name mock-msc -p 8000:8000 backend-mock-msi

## removal

<!-- container -->
docker stop mock-msc
docker rm mock-msc

<!-- image -->
docker rmi backend-mock-msc