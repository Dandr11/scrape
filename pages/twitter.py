import twint

c = twint.Config() # Настроить
c.Lang = "en" 
c.Hide_output = True
c.Username = "narendramodi" 
c.Search = ['India','bjp'] 
c.Limit = 10 
twint.run.Search(c)# Запустить
