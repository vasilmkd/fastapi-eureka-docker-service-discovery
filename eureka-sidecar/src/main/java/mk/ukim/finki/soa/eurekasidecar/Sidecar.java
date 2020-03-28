package mk.ukim.finki.soa.eurekasidecar;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.sidecar.EnableSidecar;

@SpringBootApplication
@EnableSidecar
public class Sidecar {

	public static void main(String[] args) {
		SpringApplication.run(Sidecar.class, args);
	}
}
