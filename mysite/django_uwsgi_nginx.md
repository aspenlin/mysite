notes for setting up webpage at aspenlin.com
superuser login error: attempted to write to a readonly database
solved with chmod a+w db.sqlite3
(can check read or wirte or owner with ls -l)

for static files
sudo python3 manage.py collectstatic
