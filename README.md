# Fastapi Eureka Docker service discovery

## Eureka server
Build the eureka server image:
```
cd eureka-server
./mvnw clean install
docker build -t eureka-server .
cd ..
```
Available on [localhost:8761](http://localhost:8761).

## Alice service
Build the alice service image:
```
cd service-alice
docker build -t service-alice .
cd ..
```

## Bob service
Build the bob service image:
```
cd service-bob
docker build -t service-bob .
cd ..
```

## Sidecar
Build the sidecar image:
```
cd eureka-sidecar
docker build -t eureka-sidecar .
cd ..
```

## Docker compose

### Up
Run everything with
```
docker-compose up -d
```

### Down
Stop everything with
```
docker-compose down
```

## Running services
Check running services with:
```
docker-compose ps
```

## Alice endpoints
Available on [localhost:8001](http://localhost:8001):
- `/` hello world
- `/health` (needed for eureka sidecar service registration)
- `/call-bob` (uses service discovery)

## Bob endpoints
Available on [localhost:8002](http://localhost:8002):
- `/` hello world
- `/health` (needed for eureka sidecar service registration)
- `/call-alice` (uses service discovery)
