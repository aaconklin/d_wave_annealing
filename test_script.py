from dwave.system import DWaveSampler, EmbeddingComposite
sampler_auto = EmbeddingComposite(DWaveSampler(solver={'topology__type': 'chimera'}))

h_00 = -1.115
h_11 = -1.115
h_22 = -.592
h_33 = -.592

a = -1/2 * h_00
b = -1/2 * h_22
c = -3/2 * h_33

d = -1/2 * h_11
e = -1/2 * h_33
f = -1/2 * h_33
g = h_33
i = h_33





h = {'s0': a, 's2': b, 's4': c}
J = {('s0', 's1'): d, ('s4', 's3'): e, ('s1', 's3'): f, ('s1', 's4'): g, ('s2', 's4'): i}
# Q = {**h, **J}
sampleset = sampler_auto.sample_ising(h, J, num_reads=1000)
print(sampleset)
