function s=getScale()


associated_timestamps = load('associated_timestamps.txt');


[regParams,Bfit,ErrorStats]=absor(associated_timestamps(:,[2,3,4])',associated_timestamps(:,[10,11,12])','doScale','true');

s = regParams.s;

 

end