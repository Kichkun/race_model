# Race predictor from single selfie

## Installation

```bash
git clone https://github.com/Kichkun/race_model.git
cd race_model
pip install .
```

**Race recognition** 
including asian, white, middle eastern, indian, latino and black predictions. 
```python
from race_model import RaceModel
demography = RaceModel.analyze("img4.jpg")
#demographies = DeepFace.analyze(["img1.jpg", "img2.jpg", "img3.jpg"]) #analyzing multiple faces same time
print("Race: ", demography["dominant_race"])
```

<p align="center"><img src="https://makeameme.org/media/templates/250/the_most_interesting_man_in_the_world.jpg" width="30%" height="20%"></p>

```bash
{'dominant_race': 'white',
 'race': {'asian': 1.3692333378223509e-08,
  'black': 1.682867603949867e-10,
  'indian': 1.8962782455389515e-07,
  'latino hispanic': 0.0014391415788850281,
  'middle eastern': 0.01635842927498743,
  'white': 99.98220801353455}}
```


**Pretrained weights** can be downloaded from
[here](https://drive.google.com/file/d/1aOV5LmSA7317mK14bqxvp1RJEeZWCo9S/view?usp=sharing) and should be placed in "models" folder
