python3 collect_sys_info.py &
collectpid=$!
python3 ~/rpi-realtime-peoplecount/run.py
kill $collectpid
python3 graph.py
