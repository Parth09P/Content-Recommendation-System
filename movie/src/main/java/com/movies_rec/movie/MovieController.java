package com.movies_rec.movie;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:3000")
public class MovieController {

    private final MovieService movieService;

    @Autowired
    public MovieController(MovieService movieService){
        this.movieService = movieService;
    }

    @GetMapping("/recommendation/{movieName}")
    public String getRecommendation(@PathVariable String movieName){
        return movieService.getRecommendation(movieName);
    }

    @GetMapping
    public String defaultRequest(){
        return "Home Page";
    }

}
