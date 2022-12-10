# IOET_TEST
This is the solution for the requested test

## Features
This script does a loading of *input.txt* file where are the string with work times per person.
```sh
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```
As result, this script will generates an amount for everyone's of the input file lines in console and in the *output.txt* file.
```sh
The amount to pay RENE is: 215 USD
The amount to pay ASTRID is: 85 USD
```
## Installation
IOET_TEST was made using python 3.7, requires *pytest* to run testing.

Install the dependencies with *pip*.

```sh
pip install to-requirements.txt
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Development

Keeping the principle of editable time value by day and hour, there is and dictionary with every values using the codes of days of week as key:

```sh
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
```
As a way of using of OOP for the solution, was implemented and class for input string loading and generation of results.
Class *Payment* has a attribute *in_txt* for saving of a input line of working time.
*calculate* funtion proccess the input string and load main values as worker name *in_name* and the worked hours set *in_hours*. For each of the items in the list separated by commas, the hour interval are extracted *in_start, in_end* and runs *__get_hour_value* function.
*__get_hour_value* gets the day of week code *in_day*, and the worked hours set *time_start , time_end*, then, iterates over the hours set filtering the global *DAYS* dictionary for value searching and sums the calculated amount in the variable *out_amount* for return that.
*out_format_calculate* runs *calculate* function adding to the output the requested string format.
In the main process, input file opening is made, then is iterated line by line for runing of creation of *Payment* object and generation of result with *out_format_calculate* function. Those results are writed in *output.txt* file and console.
```sh
if __name__=="__main__":
    out_file =  open("out.txt", "w")
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
```

#### Deployment

For running of the process script:

```sh
python index.py
```

For running of unit tests (has set valid and invalid input strings):

```sh
pytest test_index.py
```

Input file (has valid and invalid input strings):

```sh
input.txt
```

Output file:

```sh
output.txt
```
