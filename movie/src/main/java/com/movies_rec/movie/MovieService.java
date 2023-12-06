package com.movies_rec.movie;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class MovieService {
    private final RestTemplate restTemplate;
    private final String apiUrl = "http://localhost:8000/api/recommendation";

    @Autowired
    public MovieService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    public String getRecommendation(String movieName){
        String url = apiUrl + "/" + movieName;
        String result = restTemplate.getForObject(url, String.class);
        System.out.println(result);
        return result;
    }
}
