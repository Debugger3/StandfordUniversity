import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train=X.shape[0]
  for i in range(num_train):
	  """scores=X[i:].dot(W)
	  f_i=np.max(scores)
	  sum_i=np.sum(np.exp(scores))
	  #print sum_i.shape
	  p = lambda k: np.exp(scores[k])/ sum_i
	  exp_score=np.exp(f_i)
	  prob_scores=exp_score/sum_i"""
	  f_i = X[i].dot(W)
	  f_i -= np.max(f_i)# Normalization trick to avoid numerical instability, per http://cs231n.github.io/linear-classify/#softmax
	  #print "f_i -->",f_i
	  # Compute loss (and add to it, divided later)
	  sum_j = np.sum(np.exp(f_i))
	  #print "sum_j ",sum_j
	  p = lambda k: np.exp(f_i[k]) / sum_j
	  loss += -np.log(p(y[i]))
	  for k in xrange(W.shape[1]):
		  p_k = p(k)
		  dW[:, k] += (p_k - (k == y[i])) * X[i,:]
  loss /= num_train
  loss += 0.5 * reg * np.sum(W**2)
  dW /= num_train
  dW += reg * W
			
  #pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  #pass
  num_train=X.shape[0]
  num_class=W.shape[1]
  #print W.shape
  f=X.dot(W)
  #print f.shape
  f-=np.max(f,axis=1,keepdims=True)
  #print f.shape
  sum_f=np.sum(np.exp(f),axis=1,keepdims=True)
  #print f.shape
  p=np.exp(f)/sum_f
  loss=np.sum(-np.log(p[np.arange(num_train)]))
  
  
  #print p.shape
  ind = np.zeros_like(p)
  ind[np.arange(num_train), y] = 1
  dW = X.T.dot(p - ind)

  loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  dW /= num_train
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

