package com.movies_rec.movie;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class MovieConfig {
    @Bean
    public RestTemplate restTemplate(){
        return new RestTemplate();
    }
}
