# COVIDDataInterface
COVIDDataInterface is used to interface with Pandas to more easily access COVID data published by the New York Times


## Installation 

Use [Insert PyPI Link here]

``` bash
pip install COVIDDataInterface
```

### Requirements

Install pandas 

Use [insert PyPI link here]

```bash 
pip install pandas 
```

## Usage
``` python 

from states import states

states.getDF() # returns entire us-states dataframe from NYTimes with five columns (exlcuding index): date, state, fips (ignore), cases, deaths

states.getLength() # returns number of rows in data frame

states.getDate(index) # returns the date for the given index of a COVID-19 data entry

states.getState(index) # returns the name of the state for the given index of a COVID-19 data entry 

states.getDeathsToDate(index) # returns total number of deaths in a certain state up to the given index of a COVID-19 data entry

states.getDailyDeathCount(index) # returns the number of deaths in a certain state that happen in a single day for a given COVID-19 data entry

states.getCasesToDate(index) # returns total number of cases in a certain state up to the given index of a COVID-19 data entry

states.getDailyCaseCount(index) # returns the number of cases in a certain state that happen in a single day for a given COVID-19 data entry

states.getDateIndex(date) # returns all the indexes of a given date in the dataframe in a list

states.getStateIndex(state) # returns all the indexes of a given state in the dataframe in a list


```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT License

Copyright (c) 2021 Devon Schwartz and Neil Aylor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




