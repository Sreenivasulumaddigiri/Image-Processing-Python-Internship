import cv2
import numpy as np

# Load images
pattern_img = cv2.imread('Pattern.jpg')
flag_img = cv2.imread('Flag.jpg')

# Error handling if images fail to load
if pattern_img is None:
    raise FileNotFoundError("Pattern.jpg not found")
if flag_img is None:
    raise FileNotFoundError("Flag.jpg not found")

# Resize pattern to match flag size (if needed)
pattern_resized = cv2.resize(pattern_img, (flag_img.shape[1], flag_img.shape[0]))

# Define points for perspective transformation (simplified version)
# You would need to identify these points based on the flag's folds
pts1 = np.float32([[0, 0], [pattern_resized.shape[1], 0], [0, pattern_resized.shape[0]], [pattern_resized.shape[1], pattern_resized.shape[0]]])
pts2 = np.float32([[50, 50], [pattern_resized.shape[1]-50, 30], [50, pattern_resized.shape[0]-50], [pattern_resized.shape[1]-50, pattern_resized.shape[0]-30]])

# Apply perspective transform
matrix = cv2.getPerspectiveTransform(pts1, pts2)
warped_pattern = cv2.warpPerspective(pattern_resized, matrix, (flag_img.shape[1], flag_img.shape[0]))

# Blend the warped pattern onto the flag using alpha blending
alpha = 0.7  # Alpha for blending
output = cv2.addWeighted(flag_img, 1 - alpha, warped_pattern, alpha, 0)

# Save the result
cv2.imwrite('Output.jpg', output)

# Display the result
cv2.imshow('Mapped Pattern', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
