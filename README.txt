Build a file-based on value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop. The data store must be exposed as a library to clients that can instantiate a class and work with the data store

'd' is the dictionary in which  store data(key,value)
->create
     A new key-value pair can be added to the data store using the Create operation. 
     If already exists it will shows error message.
     The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB
     If memory exceeded and any special characters in key ,then also show error message.
->Read & Delete
     comparing the present time with expiry time.
     return the value i.e.,"key_name",value.
     Once the Time-To-Live for a key has expired,the key will no longer be available for Read operations.
->Modify
      In already created data store, modifying the key and value.
 ->Threading
      Allowed to access the data store using multiple threads, if it desires to The data store must therefore be thread-safe.

     


