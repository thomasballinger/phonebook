python main.py create test.pb
python main.py add tom 111-222-3333 -b test.pb
python main.py add kristen 11-222-333-4444-5555 -b test.pb
python main.py add lauren 1-222-333-4444 -b test.pb
python main.py lookup lauren -b test.pb
python main.py change lauren 333-4444 -b test.pb
rm test.pb
