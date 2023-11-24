package com.nano

import io.micronaut.http.HttpResponse
import io.micronaut.http.MediaType
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated

@Controller("/calculator")
@Validated
class MathController {

     @Get("/greeting")
    fun greeting(): HttpResponse<String> {
        return HttpResponse.ok("Hello world!")
    }

    @Post("/add", produces = [MediaType.APPLICATION_JSON])
    fun add(first: Int, second: Int): HttpResponse<Map<String, Int>> {
        val result = first + second
        return HttpResponse.ok(mapOf("result" to result))
    }

    @Post("/subtract", produces = [MediaType.APPLICATION_JSON])
    fun subtract(first: Int, second: Int): HttpResponse<Map<String, Int>> {
        val result = first - second
        return HttpResponse.ok(mapOf("result" to result))
    }
}
