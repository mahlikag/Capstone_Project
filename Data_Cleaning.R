Data <- read.csv("NO NAME/Sorted.csv", header = TRUE)
City <- Data$BH007
State <- Data$BH008
cities <- list()
for (i in City) {
    if (length(cities)==0) {
      cities <- append(cities,i)
    }
    else if (!i %in% cities) {
      cities <- append(cities,i)
    }
}

cities <- head(cities,-(length(cities)-100))
index <- which(City %in% cities[100])[1]
s <- State[index]
for (i in which(City %in% cities[100])) {
  if(State[i] == s) {
    iny <- i
  }
  else{
    break
  }
}


new_Data <- Data[1:iny,]

Counted <- list()
sum <- list()
AA <- list()
AA_Clear <- list()
Murder <- list()
Murder_Clear <- list()
Robbery <- list()
Robbery_Clear <- list()
index <- 1
for (i in 1:iny) {
  if(!as.character(new_Data$BH007[i]) %in% Counted) {
    Counted[index] <- as.character(new_Data$BH007[i])
    Murder[index] <-0
    Murder_Clear[index] <- 0
    AA[index] <- 0
    AA_Clear[index] <- 0
    Robbery[index] <- 0
    Robbery_Clear[index] <-0
            sum[index] <- 1
            if(new_Data$V20061[i]==91 | new_Data$V20062[i]==91 | new_Data$V20063[i] == 91) {
              Murder[index] <- 1
              if(new_Data$V1011[i]>0) {
                Murder_Clear[index] <- 1
              }
            }
            else if(new_Data$V20061[i]==131 | new_Data$V20062[i]==131 | new_Data$V20063[i] == 131) {
                AA[index] <- 1
                if(new_Data$V1011[i]>0) {
                  AA_Clear[index] <- 1
                }
              }
            else if(new_Data$V20061[i]==120 | new_Data$V20062[i]==120 | new_Data$V20063[i] == 120 ){
                  Robbery[index] <- 1
                  if(new_Data$V1011[i]>0) {
                    Robbery_Clear[index] <- 1
                  }
              }
              
            
            index <- index + 1
  }
            
  else {
    sum[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(sum[match(as.character(new_Data$BH007[i]),Counted)])
    if (new_Data$V20061[i]==91 | new_Data$V20062[i]==91 | new_Data$V20063[i] ==91) {
      Murder[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(Murder[match(as.character(new_Data$BH007[i]),Counted)]))
      if(new_Data$V1011[i]>0) {
        Murder_Clear[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(Murder_Clear[match(as.character(new_Data$BH007[i]),Counted)]))
      }
    }
    else if (new_Data$V20061[i]==131 | new_Data$V20062[i]==131 | new_Data$V20063[i]==131) {
      AA[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(AA[match(as.character(new_Data$BH007[i]),Counted)]))
      if(new_Data$V1011[i]>0) {
        AA_Clear[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(AA_Clear[match(as.character(new_Data$BH007[i]),Counted)]))
      }
    }
    else if (new_Data$V20061[i]==120 | new_Data$V20062[i]==120 | new_Data$V20063[i]==120) {
      Robbery[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(Robbery[match(as.character(new_Data$BH007[i]),Counted)]))
      if(new_Data$V1011[i]>0) {
        Robbery_Clear[match(as.character(new_Data$BH007[i]),Counted)] <- 1 + as.numeric(unlist(Robbery_Clear[match(as.character(new_Data$BH007[i]),Counted)]))
      }
    }
    
  }
   

}
final_city <- Counted
final_state <- list()
final_population <- list()
type_incidents <- list()
crime_rate <- list()
murder_perct <- list()
murder_clearance_rate <- list()
aa_perct <- list()
aa_clearance_rate <- list()
robbery_perct <- list()
robbery_clearance_rate <- list()
j <-1
for (i in final_city) {
  final_state[j] <- as.character(new_Data$BH008[match(i,new_Data$BH007)])
  final_population[j] <- as.character(new_Data$BH019[match(i,new_Data$BH007)])
  type_incidents[j] <- as.character(as.numeric(AA[j]) + as.numeric(Robbery[j]) + as.numeric(Murder[j]))
  crime_rate[j] <- (as.numeric(type_incidents[j])/as.numeric(final_population[j])) * 100000
  murder_perct[j] <- as.numeric(Murder[j])/as.numeric(type_incidents) * 100
  murder_clearance_rate[j] <- (as.numeric(Murder_Clear[j])/as.numeric(Murder[j]))*100
  aa_perct[j] <- as.numeric(AA[j])/as.numeric(type_incidents) * 100
  aa_clearance_rate[j] <- (as.numeric(AA_Clear[j])/as.numeric(AA[j]))*100
  robbery_perct[j] <- as.numeric(Robbery[j])/as.numeric(type_incidents) * 100
  robbery_clearance_rate[j] <- (as.numeric(Robbery_Clear[j])/as.numeric(Robbery[j]))*100
  j <- j + 1
  }

  
library("xlsx")

excel <- data.frame("Total Population" = matrix(unlist(final_population)), "City" = matrix(unlist(final_city)), "State" = matrix(unlist(final_state)), "Total Incidents by city" = matrix(unlist(sum)), "Total Interested Incidents by city" = matrix(unlist(type_incidents)), "Crime Rate" = matrix(unlist(crime_rate)), "Aggravated Assault Incidents" = matrix(unlist(AA)), "Aggravated Assault Percentage" = matrix(unlist(aa_perct)), "Aggravated Assault Incidents Cleared" = matrix(unlist(AA_Clear)),"Aggravated Assault Clearance Rate" = matrix(unlist(aa_clearance_rate)), "Murder/Nonnegligent Manslaughter Incidents" = matrix(unlist(Murder)), "Murder/Nonnegligent Manslaughter Percentage" = matrix(unlist(murder_perct)), "Murder/Nonnegligent Manslaughter Incidents Cleared" = matrix(unlist(Murder_Clear)),"Murder/Nonnegligent Manslaughter Clearance Rate" = matrix(unlist(murder_clearance_rate)), "Robbery Incidents" = matrix(unlist(Robbery)), "Robbery Percentage" = matrix(unlist(robbery_perct)), "Robbery Incidents Cleared" = matrix(unlist(Robbery_Clear)),"Robbery Clearance Rate" = matrix(unlist(robbery_clearance_rate)))
write.xlsx2(excel, file = "testing.xlsx", col.names = TRUE, row.names = TRUE)
