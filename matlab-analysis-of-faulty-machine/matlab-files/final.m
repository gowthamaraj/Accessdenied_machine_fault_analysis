fs = 100;                                % sample frequency (Hz)
t = 0:1/fs:10-1/fs;                      % 10 second span time vector
x = (1.3)*sin(2*pi*15*t) ...             % 15 Hz component
  + (1.7)*sin(2*pi*40*(t-2)) ...         % 40 Hz component
  + 2.5*gallery('normaldata',size(t),4); % Gaussian noise;
y = fft(x);
n = length(x);          % number of samples
f = (0:n-1)*(fs/n);     % frequency range
power = abs(y).^2/n;    % power of the DFT
%subplot(2,1,1)
plot(f,power)

xlabel('Frequency')
ylabel('Power')
y0 = fftshift(y);         
f0 = (-n/2:n/2-1)*(fs/n); 
power0 = abs(y0).^2/n;    
%subplot(2,1,2)
plot(f0,power0)
xlabel('Frequency')
ylabel('Power')
whaleFile = '.\blue.mp3';
[x,fs] = audioread(whaleFile);

plot(x);
xlabel('Sample Number')
ylabel('Amplitude')
moan = x(2.45e4:3.10e4);
t = 10*(0:1/fs:(length(moan)-1)/fs);

max(moan)
plot(t,moan)
xlabel('Time (seconds)')
ylabel('Amplitude')
xlim([0 t(end)])
m = length(moan);       % original sample length
n = pow2(nextpow2(m));  % transform length
y = fft(moan,n);        % DFT of signal
f = (0:n-1)*(fs/n)/10;
power = abs(y).^2/n;      
plot(f(1:floor(n/2)),power(1:floor(n/2)))
xlabel('Frequency')
ylabel('Power')
