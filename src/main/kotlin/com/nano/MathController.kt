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
    fun add(request: Numbers): HttpResponse<ApiResponse> {
        val result = request.first + request.second
        val response = ApiResponse(result)
        return HttpResponse.ok(response)
    }

    @Post("/subtract", produces = [MediaType.APPLICATION_JSON])
    fun subtract(request: Numbers): HttpResponse<ApiResponse> {
        val result = request.first - request.second
        val response = ApiResponse(result)
        return HttpResponse.ok(response)
    }
}

data class Numbers(val first: Double, val second: Double)

data class ApiResponse(val result: Double)
