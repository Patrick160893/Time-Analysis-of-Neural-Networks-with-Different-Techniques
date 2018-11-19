# Time-Analysis-of-Neural-netorks-with-diffreent-techniques
The following script compares the execution time of a Letter Recognition neural network for 1) with any deep-learning libraries; 2) with TensorFlow; 3) with Batching
Batching is unsurprisngly the most efficient technique in terms of execution time as it paralleizes all the iterations instead of everything been passed into the model at once, sequentially.
TensorFlow is 2nd best as the frameowrk caters for high-speed neural network architectures.
Unsurprisngly, the model without any deep-learning libary is slowest.
