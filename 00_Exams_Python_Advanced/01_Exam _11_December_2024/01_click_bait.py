"""
Technical Description (Algorithm Steps)

1. Read the input data into two collections: a deque and a stack.
2. Execute a while loop as long as both collections contain elements.
3. Retrieve the first element from the deque and the last element from the stack.
4. Determine the larger of the two elements and store its index (or origin) in a variable.
5. Compute the modulo operation between the two elements, using the larger value as the dividend
 and the smaller value as the divisor.
  5.1 Store the result in a variable named remainder.
  5.2 Append this value to a collection named final_feed.
6. If the larger element originates from the stack:
  6.1 Append the remainder as a positive value to final_feed.
  6.2 Double the remainder and push the result onto the top of the stack.
  6.3 If the doubled value equals 0, skip these operations and proceed to the next iteration.
7. If the larger element originates from the deque:
  7.1 Append the remainder as a negative value to final_feed.
  7.2 Double the remainder and append it to the end of the deque.
  7.3 If the doubled value equals 0, skip these operations and proceed to the next iteration.
8. If both extracted elements are equal:
  8.1 Append 0 to final_feed.
  8.2 Skip any reinsertion into the deque or the stack.
9. Compute total_engagement_value as the sum of all values in final_feed.
10. If total_engagement_value >= target_engagement_value, the target is considered achieved.
11. Otherwise, the target is not achieved, and a variable shortfall is calculated as:
  11.1 shortfall = target_engagement_value - total_engagement_value
12. Output the final result according to the problem requirements.
"""

from collections import deque


def process_element(greater_value, smaller_value, feed_collection, origin_collection, curr_sign):
    remainder = greater_value % smaller_value
    feed_collection.append(remainder * curr_sign)
    if remainder != 0:
        origin_collection.append(remainder * 2)


suggested_links = deque(int(x) for x in input().split())  # FIFO
featured_articles = [int(x) for x in input().split()]  # LIFO
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:
    first_element = suggested_links.popleft()
    last_element = featured_articles.pop()

    if last_element > first_element:
        sign = 1
        process_element(last_element, first_element, final_feed, featured_articles, sign)
    elif first_element > last_element:
        sign = -1
        process_element(first_element, last_element, final_feed, suggested_links, sign)
    else:
        final_feed.append(0)

total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(str(el) for el in final_feed)}")

if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")