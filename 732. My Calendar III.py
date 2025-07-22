class MyCalendarThree:

    def __init__(self):
        # Dictionary to store the difference array
        # Key: time point, Value: change in overlap count at that time
        self.diff = {}

    def book(self, startTime: int, endTime: int) -> int:
        # Add the new event to our difference array
        # At startTime, overlap count increases by 1
        self.diff[startTime] = self.diff.get(startTime, 0) + 1
        # At endTime, overlap count decreases by 1
        self.diff[endTime] = self.diff.get(endTime, 0) - 1
        
        # Calculate the maximum overlap by sweeping through all time points
        max_overlap = 0
        current_overlap = 0
        
        # Process all time points in sorted order
        for time in sorted(self.diff.keys()):
            current_overlap += self.diff[time]
            max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Basic functionality
    calendar = MyCalendarThree()
    
    # Book [10, 20) -> should return 1 (only one event)
    print(f"Book [10, 20): {calendar.book(10, 20)}")
    
    # Book [50, 60) -> should return 1 (no overlap with first event)
    print(f"Book [50, 60): {calendar.book(50, 60)}")
    
    # Book [10, 40) -> should return 2 (overlaps with [10, 20) from 10-20)
    print(f"Book [10, 40): {calendar.book(10, 40)}")
    
    # Book [5, 15) -> should return 3 (overlaps with both previous events from 10-15)
    print(f"Book [5, 15): {calendar.book(5, 15)}")
    
    # Book [5, 10) -> should return 3 (overlaps at point 5-10, but doesn't increase max)
    print(f"Book [5, 10): {calendar.book(5, 10)}")
    
    # Book [25, 55) -> should return 3 (creates new overlaps but doesn't exceed 3)
    print(f"Book [25, 55): {calendar.book(25, 55)}")
    
    print("\n" + "="*50)
    
    # Test case 2: Edge cases
    calendar2 = MyCalendarThree()
    
    # Same start and end times (but different ranges)
    print(f"Book [0, 1): {calendar2.book(0, 1)}")
    print(f"Book [0, 1): {calendar2.book(0, 1)}")  # Exact same event
    print(f"Book [0, 1): {calendar2.book(0, 1)}")  # Third identical event
    
    print("\n" + "="*50)
    
    # Test case 3: Large numbers (within constraints)
    calendar3 = MyCalendarThree()
    print(f"Book [1000000000, 1000000001): {calendar3.book(1000000000, 1000000001)}")
    print(f"Book [999999999, 1000000001): {calendar3.book(999999999, 1000000001)}")
