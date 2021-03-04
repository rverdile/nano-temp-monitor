python3 collect_sys_info.py &
collectpid=$!
python3 ~/fisheye-nano-rapid/example.py
kill $collectpid
python3 graph.py
