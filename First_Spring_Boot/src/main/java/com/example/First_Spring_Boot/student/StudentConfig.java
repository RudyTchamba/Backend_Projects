package com.example.First_Spring_Boot.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository) {
        return args -> {
            Student rudy = new Student(
                    "Rudy",
                    "rudytchamba@gmail.com",
                    LocalDate.of(2002, Month.JANUARY, 5)
            );

            Student chakra = new Student(
                    "Chakra",
                    "chakra@gmail.com",
                    LocalDate.of(2001, Month.DECEMBER, 31)
            );

            repository.saveAll(
                    List.of(rudy, chakra)
            );
        };
    }
}
