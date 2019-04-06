# R script for plotting one of the algorithm questions on the Coursera week 1 drill
# to be honest I don't quite get it so I want to see a graph


# Example question: 

# Arrange the following functions in increasing order of growth rate
# a: sqrt(n)
# b: 10^n
# c: n^1.5
# d: 2^sqrt(log(n))
# e: n^5/3

df = data.frame(n=(1:1000)/20)
df$a <- sqrt(2^(2^df$n))
df$b <- 2^(df$n^2)
df$c <- df$n^2*(log(df$n, base=2))
df$d <- df$n
df$e <- (df$n^2)^df$n

for (cur_col in colnames(df)) {
  df[is.infinite(df[,cur_col]), cur_col] <- 100000
  df[df[,cur_col] > 100000, cur_col] <- 100000

}

plot(df$n, df$a, type="l", col="brown", lwd=3)
lines(df$n, df$b, col="darkgreen", lwd=3)
lines(df$n, df$c, col="purple", lwd=3)
lines(df$n, df$d, col="blue", lwd=3)
lines(df$n, df$e, col="orange", lwd=3)


# I answered "acedb" which was incorrect
# I thought 'd' would be fast growing since n is an exponent but it's the smallest function for large n
# The other 4 at least I ranked correctly

# Looking at the graph, I should have answered:
# fastest growing: green (aka B) <- correct
# 2nd fastest: orange (aka E) <- incorrect
# 3rd fastest: purple (aka C) <- incorrect
# 4th fastest: brown(aka A) <- incorrect
# 5th fastest: blue (aka D)

# So the correct answer was daceb
