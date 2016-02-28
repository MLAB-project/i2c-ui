;; Auto-generated. Do not edit!


(when (boundp 'sensor_server::GetSensVal)
  (if (not (find-package "SENSOR_SERVER"))
    (make-package "SENSOR_SERVER"))
  (shadow 'GetSensVal (find-package "SENSOR_SERVER")))
(unless (find-package "SENSOR_SERVER::GETSENSVAL")
  (make-package "SENSOR_SERVER::GETSENSVAL"))
(unless (find-package "SENSOR_SERVER::GETSENSVALREQUEST")
  (make-package "SENSOR_SERVER::GETSENSVALREQUEST"))
(unless (find-package "SENSOR_SERVER::GETSENSVALRESPONSE")
  (make-package "SENSOR_SERVER::GETSENSVALRESPONSE"))

(in-package "ROS")





(defclass sensor_server::GetSensValRequest
  :super ros::object
  :slots (_name _data ))

(defmethod sensor_server::GetSensValRequest
  (:init
   (&key
    ((:name __name) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _data (string __data))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass sensor_server::GetSensValResponse
  :super ros::object
  :slots (_val ))

(defmethod sensor_server::GetSensValResponse
  (:init
   (&key
    ((:val __val) 0)
    )
   (send-super :init)
   (setq _val (round __val))
   self)
  (:val
   (&optional __val)
   (if __val (setq _val __val)) _val)
  (:serialization-length
   ()
   (+
    ;; int64 _val
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _val
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _val (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _val) (= (length (_val . bv)) 2)) ;; bignum
              (write-long (ash (elt (_val . bv) 0) 0) s)
              (write-long (ash (elt (_val . bv) 1) -1) s))
             ((and (class _val) (= (length (_val . bv)) 1)) ;; big1
              (write-long (elt (_val . bv) 0) s)
              (write-long (if (>= _val 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _val s)(write-long (if (>= _val 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _val
#+(or :alpha :irix6 :x86_64)
      (setf _val (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _val (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass sensor_server::GetSensVal
  :super ros::object
  :slots ())

(setf (get sensor_server::GetSensVal :md5sum-) "1bc3537bb8034a7562e9cc5973528637")
(setf (get sensor_server::GetSensVal :datatype-) "sensor_server/GetSensVal")
(setf (get sensor_server::GetSensVal :request) sensor_server::GetSensValRequest)
(setf (get sensor_server::GetSensVal :response) sensor_server::GetSensValResponse)

(defmethod sensor_server::GetSensValRequest
  (:response () (instance sensor_server::GetSensValResponse :init)))

(setf (get sensor_server::GetSensValRequest :md5sum-) "1bc3537bb8034a7562e9cc5973528637")
(setf (get sensor_server::GetSensValRequest :datatype-) "sensor_server/GetSensValRequest")
(setf (get sensor_server::GetSensValRequest :definition-)
      "string name
string data
---
int64 val

")

(setf (get sensor_server::GetSensValResponse :md5sum-) "1bc3537bb8034a7562e9cc5973528637")
(setf (get sensor_server::GetSensValResponse :datatype-) "sensor_server/GetSensValResponse")
(setf (get sensor_server::GetSensValResponse :definition-)
      "string name
string data
---
int64 val

")



(provide :sensor_server/GetSensVal "1bc3537bb8034a7562e9cc5973528637")


