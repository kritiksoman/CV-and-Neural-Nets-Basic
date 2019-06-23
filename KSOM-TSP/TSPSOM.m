clc
clear all
close all

%% load city locations from csv file
[CityNo,cityx,cityy] = importfile('data.csv');
numCity=length(cityx);
scatter(cityx,cityy,'b','filled');
dx = 0.75e2; dy = dx; % displacement so the text does not overlay the data points
for i=1:length(cityx)
    c = cellstr(string(i));
    text(cityx(i)+dx, cityy(i)+dy, c);
end
title('TSP using KSOM');
grid on;xlabel('X Coordinate');ylabel('Y Coordinate');

%% initializations
etah0=30;
tauh=10;
etaw0=.7;
tauw=40;

wx(1)=0;
wy(1)=0;
hold on;
winNeuronCount(1) = 0;%array to store number of times a winning neuron has been updated
neuronCount(1) = 0; %array to store number of times a neuron has been updated
iterations = 100;

%% Algorithm
for e=1:iterations
    etah=etah0*exp(-e/tauh);   
    etaw=etaw0*exp(-e/tauw);
    d=[];
    for idx = 1 :length(winNeuronCount)  %clear count
        winNeuronCount(idx) = 0;
    end

    for i = 1:numCity
        %find winning neuron for current city
        distance=(cityx(i)-wx).^2+(cityy(i)-wy).^2;
        [min_dis,winIdx]=min(distance);
        
        %creation of new neuron if winning neuron has already been updated
        %in earlier iteration
        if winNeuronCount(winIdx) >= 1  % if find same node, duplicate it
            wx = [wx(1:winIdx) wx(winIdx) wx(winIdx+1:end)];
            wy = [wy(1:winIdx) wy(winIdx) wy(winIdx+1:end)];
            distance = [distance(1:winIdx) distance(winIdx) distance(winIdx+1:end)];
            winNeuronCount = [winNeuronCount(1:winIdx) 0 winNeuronCount(winIdx+1:end)];
            neuronCount = [neuronCount(1:winIdx) 0 neuronCount(winIdx+1:end)];
            winIdx = winIdx+1; %duplicated node
        end
                
        %Find distance from winning neuron
        for idx = 1 : size(wx,2)
            d(idx) = min (mod((idx-winIdx),size(wx,2)),mod((winIdx-idx),size(wx,2)));
        end        
        
        h=exp(-(d.^2)/etah^2);
        %Update weights
        for q = 1 : size(wx,2)
            wx(q)=wx(q)+etaw*h(q)*(cityx(i)- wx(q));
            wy(q)=wy(q)+etaw*h(q)*(cityy(i)- wy(q));
        end
        winNeuronCount(winIdx) =  winNeuronCount(winIdx) + 1;
        
    end
 
    neuronCount= neuronCount + ones(size(neuronCount));
    %Keep neurons that won once
    neuronCount(winNeuronCount>0) = 0;
    
    %Delete neurons that got updated more than twice but did not win
    wx(neuronCount>2) = [];
    wy(neuronCount>2) = [];
    distance(neuronCount>2) = [];
    winNeuronCount(neuronCount>2) = [];
    neuronCount(neuronCount>2) = [];
    
    %Plot
    scatter(cityx,cityy,'b','filled');
    hold on;
    plot(wx,wy,'ro');
    plot([wx wx(1)],[wy wy(1)],'k','linewidth',2);
    hold off
    title('TSP using KSOM');
    grid on;xlabel('X Coordinate');ylabel('Y Coordinate');
    drawnow;

end
xCoordRing=[wx wx(1)];
yCoordRing=[wy wy(1)];
totalDist = 0;
for i = 1 : numCity
    totalDist =  totalDist + sqrt((xCoordRing(i)-xCoordRing(i+1))^2+(yCoordRing(i)-yCoordRing(i+1))^2);
end
disp('Total distance : ');
disp(totalDist);

for i=1:length(cityx)
    c = cellstr(string(i));
    text(cityx(i)+dx, cityy(i)+dy, c);
end
title('TSP using KSOM');
grid on;xlabel('X Coordinate');ylabel('Y Coordinate');
