'''

The highway adjacent to Farmer John's farm has recently seen a dramatic increase in traffic, or at least so it seems to Farmer John. To be sure, he wants to measure the traffic flow on the highway with a set of sensors, each capable of measuring the rate of flow of traffic on a segment of road.
Unfortunately, while walking through the barn one day, Farmer John trips and drops his box of sensors into a large vat of milk, after which they no longer work as well. Instead of producing a single exact reading of traffic flow rate, each sensor now outputs a range of possible values. For example, a sensor might output the range [7,13], indicating that the rate of traffic flow on a segment of road is no less than 7, and no greater than 13.

The highway runs for N miles next to the farm, and traffic on the highway only flows in one direction, from mile 1 towards mile N. Farmer John wants to install N sensors -- one for each 1-mile segment of the highway. In some of these segments, there are on-ramps that allow traffic to enter the highway; in each of these cases, Farmer John will install his sensor on the on-ramp to measure (approximately) the amount of incoming traffic. In some segments there are off-ramps that allows traffic to exit the highway; in each of these cases, Farmer John will install his sensor on the off-ramp. Each segment contains at most one ramp. If there is no on-ramp or off-ramp in a segment of highway, Farmer John installs a sensor on the main highway itself.

Given the readings from Farmer John's N sensors, please determine the most specific possible ranges that describe the rate of traffic flow initially on the highway prior to mile 1 and for traffic continuing on the highway past mile N. These ranges should be consistent with all N sensor readings.

INPUT FORMAT (file traffic.in):
The first line of input contains N (1≤N≤100). Each of the remaining N lines describes a 1-mile segment of the road, in order from mile 1 to mile N. Each line contains a string that is either "on" (if there is an on-ramp on this segment), "off" (if there is an off-ramp), or "none" (if there is no ramp), followed by two integers in the range 0…1000, indicating the lower and upper endpoints of the sensor range from this segment. If the segment contains a ramp, the sensor reading is from the ramp. Otherwise, it is from the main highway. At least one of the highway segments will be designated as "none".
OUTPUT FORMAT (file traffic.out):
The first line of output should contain two integers giving the most specific range possible for the rate of traffic flow prior to mile 1. The second line of output should contain two integers giving the most specific range possible for the rate of traffic flow after mile N. A valid solution is always guaranteed to exist.
SAMPLE INPUT:
4
on 1 1
none 10 14
none 11 15
off 2 3
SAMPLE OUTPUT:
10 13
8 12
In this example, the combination of readings from segments 2 and 3 tell us that the flow rate through these segments is somewhere in the range [11,14], since only this range is consistent with both the readings [10,14] and [11,15]. In mile 1, exactly 1 unit of flow enters on an on-ramp, so prior to mile 1, the flow rate must be in the range [10,13]. In mile 4, between 2 and 3 units exits on an off-ramp, so the range of possible flow rates after this is [8,12].

Problem credits: Brian Dean

'''
data = []
for i in range(int(input())):
    line = input().split()
    line[1] = int(line[1])
    line[2] = int(line[2])
    data.append(line)

currentLowest = 0
currentHighest = 999

for i in range(len(data) - 1, -1, -1):
    if data[i][0] == "none":
        if data[i][1] > currentLowest:
            currentLowest = data[i][1]
        if data[i][2] < currentHighest:
            currentHighest = data[i][2]
    elif data[i][0] == "on":
        currentLowest -= data[i][2]
        currentHighest -= data[i][1]
    elif data[i][0] == "off":
        currentLowest += data[i][1]
        currentHighest += data[i][2]
print(currentLowest, currentHighest)

for i in range(len(data)):
    if data[i][0] == "none":
        if data[i][1] > currentLowest:
            currentLowest = data[i][1]
        if data[i][2] < currentHighest:
            currentHighest = data[i][2]
    elif data[i][0] == "on":
        currentLowest += data[i][1]
        currentHighest += data[i][2]
    elif data[i][0] == "off":
        currentLowest -= data[i][2]
        currentHighest -= data[i][1]
print(currentLowest, currentHighest)