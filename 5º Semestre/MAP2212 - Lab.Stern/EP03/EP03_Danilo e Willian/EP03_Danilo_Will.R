#--------------------------------------------------------------
#Danilo Brito da Silva - 10693250
#Yugo Oyama - 9297784
#--------------------------------------------------------------
#EP03 - Método de Monte Carlos - Quasi aleatório

library(ggplot2)
library(randtoolbox)
library(rngWELL)
#Função que desejamos integrar no intervalo [0,1]
f <- function(x)
{
  a <- 0.442705074
  b <- 0.10693250
  return(exp(-a*x)*cos(b*x))
}
#----------1.Crud----------
n <- 5    #amostra incial
erro_crud <- 1     #erro inicial
while(erro_crud > 0.0005)
{                                   # n será incrementado até que erro_crud < 0.0005
  vetorx <- vector("numeric", n)    # criação de vetor de tamanho n 
  x <- halton(n,1) #gerando sequencia de variável quasi-aleatória em [0,1]
  for (i in 0:n){
    vetorx[i] <- f(x[i]) #vetor recebe f(x)
  }
  erro_crud <- sqrt(var(vetorx)/n) #cálculo do erro
  if (erro_crud > 0.0005)
  {
    n <- n*2
  }
}
estimativa_g_crud <- mean(vetorx)
print(n)
print(estimativa_g_crud)
print(erro_crud)

#----------2.Hit or Miss----------
n <- 5  #amostra incial
erro_hit  <- 1 #erro inicial
while(erro_hit > 0.01){ 
  vetor_x <- halton(n, 1, init = FALSE)
  vetor_y <- halton(n, 1, init = FALSE)
  vetor_n <- vector("numeric", n)
  vetor_f <- vector("numeric", n)
  
  for (i in 1:n){
    vetor_f[i] <- f(vetor_x[i])
  }
  for (i in 1:n){ #armazenando valores de n*
    if (vetor_f[i] >= vetor_y[i]){
      vetor_n[i] = 1
    }
    else{vetor_n[i] = 0}
  }
  erro_hit = sqrt(var(vetor_n)/n) #cálculo do erro
  if (erro_hit > 0.0005){
    n <- n*2
  }
}
estimativa_g_hit = mean(vetor_n)

print(n)
print(estimativa_g_hit)
print(erro_hit)

#----------3.Importance Sampling----------
n <- 5  #amostra incial
erro_is <- 1 #erro inicial

#v_x <- vector("numeric", n) #vetor de n variáveis xi uniformes no intervalo [0,1]
v_weight <- vector("numeric",n) #vetor com peso de importancia (importance weight) para cada valor amostrado

while(erro_is > 0.0005){
  v_x <- halton(n,1) #armazena n variáveis pseudo aletatórias
  for (i in 0:n){
    v_weight[i] <- (f(v_x[i]))/dbeta(v_x[i],0.9,1.1)
  }
  
  erro_is <- sqrt(var(v_weight)/n) # calcula o erro do método
  if (erro_is > 0.0005){
    n <- n*2
  }
}

estimativa_g_is <- mean(v_weight)

print(n)
print(estimativa_g_is)
print(erro_is)

# Gera um gráfico comparando a função densidade da beta (x, 0.9,1.1) e a f(x)
x<- seq(0,1,length.out = 400)
plot(x,f(x),'l', xlab = 'x', ylab = 'f(x) | dbeta ')
curve(dbeta(x,0.9,1.1), add = TRUE, col = 'red')
legend("topright", legend=c("beta", "f(x)"),text.col=c("red", "black"),col =c("red", "black"))

#----------4.Control Variate----------  
n <- 5
erro_cv <- 1

#Criando função phi:
phi = function(x){
  return (1 - (0.5*x))
}

# Método iterativo:
while (erro_cv > 0.0005)
{
  v_x   <- halton(n,1) #vetor de n variáveis quasi-aleatórias
  v_phi <- vector("numeric",n) #vetor com valores da phi (xi)
  v_f   <- vector("numeric",n) #vectorcom valores da f(xi)
  
  for (i in 0:n)
  {
    v_phi[i] <- phi(v_x[i]) #vetor que armazena os valores de phi(xi)
    v_f[i]   <- f(v_x[i])   #vetor que armazena os valores da f(xi)
  }
  var <- var(v_phi) + var(v_f) - 2*var(v_phi,v_f) # variância da diferença de f e phi
  erro_cv <- sqrt(var/n)                          #cálculo do erro
  if (erro_cv > 0.0005)
  {
    n <- n*2
  }
}
v_dif <- f(v_x) - phi(v_x)
estimativa_g_cv <- mean(v_phi) + mean(v_dif)

print(n)
print(estimativa_g_cv)
print(erro_cv)

#Gráfico comparando phi(x) e f(x)
x<- seq(0,1,length.out = 1000)
plot(x,f(x),'l', xlab = 'x', ylab = 'f(x)', col = "blue")
curve(phi(x), add = TRUE, col = 'red')
legend("topright", legend=c("φ(x)", "f(x)"),text.col=c("red", "blue"),col =c("red", "blue"))

