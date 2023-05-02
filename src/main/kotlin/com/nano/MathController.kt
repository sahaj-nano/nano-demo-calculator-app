package com.nano

import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Post
import io.micronaut.validation.Validated
import javax.validation.constraints.NotNull

@Controller("/calculator")
@Validated
class MathController {
    @Post("/add")
    fun add(@Body @NotNull numbers: Numbers): Int {
        return numbers.first + numbers.second
    }

    @Post("/subtract")
    fun subtract(@Body @NotNull numbers: Numbers): Int {
        return numbers.first - numbers.second
    }
}
