docker build -t backend-mock-msi .

docker run -d --name mock-msc -p 8000:8000 backend-mock-msi