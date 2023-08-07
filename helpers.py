import re

# check whether a string looks like a year value
# return the integer value of the year if so

def getYear(year):
   digits = re.compile("^\d{4}$")
   if not digits.match(year):
      return None
   else:
      return int(year)

# Helper function for ./genre
def maxLength(Genres):
   length = 0
   for genre in Genres:
      if genre[1] > length:
         length = genre[1]
   return length

# Helper function for ./movies
def unique_ID(Movies_Acted):
   list_unique = []
   list_duplicates = []
   l = []
   
   for i in Movies_Acted:
      if i not in list_unique:
         list_unique.append(i)
      else:
         list_duplicates.append(i)

   for i in list_duplicates:
         for j in i:
            l.append(j)

   return list_unique


# Helper function for ./movie
def printPrincipals(cur, Movie_ID, query_one_id, query_has_role, query_if_actor, 
                    query_principals_no_role):
   # Given the movie ID, get the principals
   cur.execute(query_one_id, [Movie_ID])
   Movie_Info = cur.fetchall()
   
   # Get the movie name and year and then print
   Movie_Name = Movie_Info[0][1]
   Movie_Year = str(Movie_Info[0][2])
   print(Movie_Name, '(' + Movie_Year + ')')
   
   
   # Print the principals that have a role
   for person in Movie_Info:
      Person_ID = person[5]
      Person_Name = person[0]
      
      # Find the principals that have a role
      cur.execute(query_has_role, [Movie_ID, Person_ID])
      Has_Role = cur.fetchone()
      
      # Find the principals that do not have a role
      cur.execute(query_principals_no_role, [Movie_ID, Person_ID, Movie_ID, 
                                             Person_ID])
      No_Role_Principal = cur.fetchone()
      
      # Check if person is an actor for the ??? case
      cur.execute(query_if_actor, [Movie_ID, Person_ID])
      If_Actor = cur.fetchone()
      
      # Print the principals with roles
      if Has_Role:
         Person_Role = Has_Role[1]
         print(Person_Name, 'plays', Person_Role)
         
      # Print the principals that do not have roles
      if No_Role_Principal:
         Person_Job = No_Role_Principal[1]
         print(Person_Name + ':', Person_Job)
      
      # Print the actor whomst role is unknown
      if If_Actor and not Has_Role:
         print(Person_Name, 'plays ???')
  