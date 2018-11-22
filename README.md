# farm-simulator
This project intended to siumulate the growth of crops.
The idea was to monitor and track changes during the cultivation time to assess and predict yields and risk of crop failures.

## Introduction
The project was to develop a crop growth simulator that takes into consideration many factors that would affect the growth and development of any crop.

### Those factors considered are:
* Solar radiation or light intensity
* Weather variables (air temperature, humidity, atmospheric pressure and wind speed)
* Soil variables (pH, EC, moisture, temperature, water flow or retention)

### Explanation
* The idea was to be able to check through an application how the real crop that is grown outsite your house or in your farm, meaning that with a pool of sensors contanstly monitoring the crop's weather and soil data and taking pictures of the crops daily would allow to monitor growth of fuits and plant etc and develop a model that can predict crop failures and estimate real-time yields at any moment during the cultivation cycle.  

### NOTE
* The farm simulator is currently unfinished and probably no more work will be done at this project for now.
* The farm simulator currently makes up variables such as nutrients found in the soil, or solar radiation or weather information and applies factors to determine growth and development of the crop just to make the simulator run, however, formulas etc used from the agricultural side are fictional.

### EXAMPLE CODE

## STEP 1
### CREATING USER NAMED "carlos"
```python
carlos = {
	'name'		 : 'Carlos',
	'location'	 : 'Venezuela',
	'email'		 : 'email1@hotmail.com',
	'birthday'	 : '27-02-1986',
	'mobile'	 : '+491765555555',
	'emailRecovery'	 : 'email2@gmail.com',
	}
      
carlos = User(**carlos)
```

## STEP 2
### CREATING FARM NAMED "AQUAPONIC"
```python
carlos.farm_new('AQUAPONIC', 'Indonesia')
print(carlos.farms['AQUAPONIC'].info())
```


## STEP 3
### USE THE FARMER TO PREPARE A CROP
```python
carlos.farms['AQUAPONIC'].farmer.prepare_crop(10,	'Plum', 5) # (growth area, 'crop', batches for multi harvest)
```


## STEP 4
### USE THE FARMER TO START FARM SIMULATION
```python
sim_data = {
		'qtyDays' 	: 180, # this refers to the qty of days that would a tomato to grow from seed until harvest
		'mineralTag'   	: 'Mg',
		'mineralValue' 	: 3,
		'water'		: 250,
		'hours' 	: 10,
			}
carlos.farms['AQUAPONIC'].farmer.sim_time('Plum', **sim_data)
```

## STEP 5
### USE THE FARMER TO GET YOU A REPORT OF THE FARM SIMULATION
```python
carlos.farms['AQUAPONIC'].farmer.report('Plum')
```
