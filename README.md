# Android-PIN-BruteForce
Python script to brute force Android Pin Lock

# Step 1
Create adb access to a rooted android device. Santoku can be used to get this done

# Step 2
Pull settings.db from phone using 'adb pull /data/data/com.android.providers.setings/databases/settings.db' . The db is a sqllite db and it contains a tabled named "secure". Secure has a locksettings filed that contains the password salt. 

# Step 3
Pull password hash using 'adb pull /data/system/password.key'. This contains MD5 & SHA1 hashes.

# Step 4
Pull device password policy using 'adb pull /data/system/device_policies.xml'. This contains PIN length, complexity etc.

# Step 5
Run the python script with files from steps 1-4 and .py script in the same folder and it will crack the password.
