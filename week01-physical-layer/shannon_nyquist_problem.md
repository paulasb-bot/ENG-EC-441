PHYSICAL LAYER – BANDWITH, NOISE, DATA RATE 

PROBLEM STATEMENT
A communication channel has a bandwidth of 1 MHz.
1. If the signal-to-noise ratio (SNR) is 30 dB, what is the maximum data rate according to Shannon’s Theorem?
2. If the channel is noiseless and we use 16 signal levels, what is the maximum data rate according to Nyquist’s Theorem?
3. Which limit is more restrictive in this case? Why?

SOLUTION
Step 1: Shannon Capacity
Shannon’s Theorem:
C = B · log₂(1 + SNR)

Where:
B = 1 MHz = 10⁶ Hz
SNR must be converted from dB to linear scale.

SNR_linear = 10^(SNR_dB / 10)
SNR_linear = 10^(30 / 10) = 10³ = 1000

C = 10⁶ · log₂(1 + 1000)
C = 10⁶ · log₂(1001)
C ≈ 10⁶ · 9.97
C ≈ 9.97 Mbps
Step 2: Nyquist Capacity
Nyquist Theorem (Noiseless Channel):
C = 2B · log₂(M)

Where:
B = 1 MHz = 10⁶ Hz
M = 16 signal levels

C = 2 · 10⁶ · log₂(16)
C = 2 · 10⁶ · 4
C = 8 Mbps
Step 3: Comparison
The Nyquist limit (8 Mbps) is lower than the Shannon limit (≈ 9.97 Mbps).
Therefore, the Nyquist limit is more restrictive in this case. Even though the channel could theoretically support nearly 10 Mbps considering noise, using only 16 signal levels restricts the maximum achievable data rate to 8 Mbps.
Although Shannon capacity is higher than Nyquist in this scenario, increasing the number of signal levels is not always trivial.
If we increase M, the symbols become closer together in amplitude or phase, making the system more sensitive to noise. Therefore:

• Increasing M increases theoretical data rate.                                                                 .
• But higher M requires higher SNR to maintain low error probability. 
This illustrates a fundamental tradeoff in communication systems: Capacity, modulation complexity, and noise tolerance are tightly connected. 
In practice, modulation schemes (e.g., QPSK, 16-QAM, 64-QAM) are chosen depending on channel conditions. 


REFLECTION
This example highlights the difference between two fundamental communication limits:

• Shannon’s Theorem accounts for noise and defines the absolute theoretical capacity of a noisy channel.
• Nyquist’s Theorem applies to noiseless channels and shows how the number of signal levels limits the data rate.

In real systems, both constraints must be considered. Engineers select modulation schemes (number of signal levels) while accounting for noise to approach Shannon capacity without exceeding practical limits.
