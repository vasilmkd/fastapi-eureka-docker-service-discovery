FROM openjdk:8-jre-slim
ENV SERVICE_NAME=alice
ARG JAR_FILE=target/eureka-sidecar*.jar
COPY ${JAR_FILE} eureka-sidecar.jar
EXPOSE 5678
ENTRYPOINT ["java", "-jar", "/eureka-sidecar.jar"]