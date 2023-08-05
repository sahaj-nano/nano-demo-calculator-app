package com.nano

import javax.validation.constraints.NotNull

data class Numbers(
    @field:NotNull val first: Int,
    @field:NotNull val second: Int
)
