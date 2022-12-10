from datetime import datetime, date, time, timedelta

DAYS={
        "MO": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 25} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 15} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 20} , 
              ],
        "TU": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 25} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 15} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 20} , 
              ],
        "WE": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 25} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 15} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 20} , 
              ],
        "TH": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 25} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 15} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 20} , 
              ],
        "FR": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 25} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 15} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 20} , 
              ],
        "SA": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 30} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 20} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 25} , 
              ],
        "SU": [
                {"hours" : ["00:01" ,  "09:00"] , "amount" : 30} , 
                {"hours" : ["09:01" ,  "18:00"] , "amount" : 20} , 
                {"hours" : ["18:01" ,  "00:00"] , "amount" : 25} , 
              ]
      }

class Payment:

    def __init__(self, in_txt):
            self.in_txt = in_txt

    def calculate(self):
        """Calculates an amount from working days

        Returns:
            str: Name of worker.
            int: Amount of payment.
        """    
        out_amount = 0
        in_name = ""
        try:
            in_name , in_hours  = self.in_txt.split("=")
            for in_hour in in_hours.split(","):
                in_day = in_hour[0:2]
                in_start, in_end = in_hour[2:].split("-")
                out_amount += self.__get_hour_value(in_day , time.fromisoformat(in_start) , time.fromisoformat(in_end))
            return in_name , out_amount
        except:
            raise 
    
    def __get_hour_value(self, in_day , time_start , time_end):
        """Calculate the cost of working time in one day
        
        Args:
            mydb ([type]): [description]
            mycursor ([type]): [description]
            in_day (str): Code of day of week.
            time_start (datetime.time): Start of working time.
            time_end (datetime.time): Finish of working time.
    
        Returns:
            str: Name of worker.
            int: Amount of payment.
        """   
        out_amount = 0
        time_end = time(23, 59) if time_end == time(00, 00) else time_end
        while(time_start < time_end):
            try:
                if(time_start.hour < 23):
                    time_start = (datetime.combine(date.today(), time_start) + timedelta(hours=1)).time()
                else:
                    time_start = time(23, 59)
                out_amount += list(filter(lambda d: ((time.fromisoformat(d["hours"][0]) <= time_start) and (d["hours"][1] == "00:00") ) or (time.fromisoformat(d["hours"][0]) <= time_start <= time.fromisoformat(d["hours"][1])) , DAYS[in_day] ))[0]["amount"]
            except:
                print("An error occurred while looking up the time value")
        return out_amount  
    
    def out_format_calculate(self):
        """Calculates an amount from working days and generates an output format string

        Returns:
            str: name and amount in required format string
        """  
        name , amount = self.calculate()
        return ("The amount to pay "+name+" is: "+str(amount)+" USD")
    
if __name__=="__main__":
    out_file =  open("output.txt", "w")
    with open("input.txt") as file:
        for line in file:
            try:
                pay = Payment( line.strip())
                result = pay.out_format_calculate()
                out_file.write(result + "\n")
                print(result)
            except Exception as e:
                out_file.write(str(e) + "\n")
                print(e)
    out_file.close()