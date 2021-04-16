.PHONY: nb jt
dep:
	pip install -r requirements.txt
nb:
	jupyter notebook --no-browser --port=8881 --allow-root --ip=0.0.0.0 >> /tmp/jp.log 2>&1 &
	sleep 3 && wget localhost:8881 && jt -t solarizedl -T
