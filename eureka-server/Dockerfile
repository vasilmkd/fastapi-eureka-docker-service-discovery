FROM openjdk:8-jre-slim
ARG JAR_FILE=target/eureka-server*.jar
COPY ${JAR_FILE} eureka-server.jar
EXPOSE 8761
ENTRYPOINT ["java", "-jar", "/eureka-server.jar"]