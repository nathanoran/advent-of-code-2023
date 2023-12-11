<h1>Camel Cards</h1>

Solutions to [day 7 problems](https://adventofcode.com/2023/day/7)

<h2>Notes on implementation</h2>

Since this is our last day in Python, I decided to approach this puzzle in a way to apply as much as I've learned so far.

<h3>Part 1 (Jacks) and General Approach</h3>

<h4>The Hand class</h4>

I created a `Hand` class so that it tracks the state of a single hand. The class has four properties:

 - `cards` This is the raw string of cards from the `camel-cards.txt` file
 - `bid` This is the bet placed on this hand
 - `cardCounts` This is a dictionary that tracks the number of instances of each card value per hand. Once we have this structure, determining the hand type becomes fairly simple.
    - `32T3K` would result in a `cardCounts` object like this: `{"3": 2, "2": 1, "T": 1, "K": 1}`
 - `type` This is a numeric value that represents the type of a hand outlined by the camel cards rules. (Might be worth making this an enum, but since I am the only person looking at this and this was just a faster I did not)
    - `6`: Five of a kind
    - `5`: Four of a kind
    - `4`: Full House
    - `3`: Three of a kind
    - `2`: Two Pairs
    - `1`: One Pair
    - `0`: High Card

<h5>Determining the hand type</h5>

To determine the `type` of a hand, the hand class has a `getType` method. This method works down the list above and returns the highest number that the hand qualifies for.

The `getType` method uses six boolean methods that evaluates the `cardCounts` to determine whether the hand meets the criteria for that type. Since we know that every hand has exactly five cards, we can determine this based on the `cardCounts` dict the hand type for any hand.

<h6>Is Five of a Kind</h6>

The highest valued type of hand is five of a kind. This means that all five cards in a hand have the same value. A `cardCounts` dict would look like this `{"K": 5}`. So, we can determine whether a hand is a Five of a Kind type if there is only one entry in the `cardCounts` dict.

<h6>Is Four of a Kind</h6>

The second highest valued type of hand is four of a kind. This means that four cards in a hand have the same value. A `cardCounts` dict would look like this `{"K": 4, "Q": 1}`. So, we can determine whether a hand is a Four of a Kind type if there are only two entries in the `cardCounts` dict and one of those entries has a value of `4`.

<h6>Is Full House</h6>

The third highest valued type of hand is the full house. This means that 3 cards in a hand have the same value and the other 2 cards are a pair. A `cardCounts` dict would look like this `{"K": 3, "Q": 2}`. So, we can determine whether a hand is a Full House type if there are only two entries in the `cardCounts` dict and one of those entries has a value of `3`.

<h6>Is Three of a Kind</h6>

The fourth highest valued type of hand is three of a kind. This means that 3 cards in a hand have the same value and the other 2 cards are not a pair. A `cardCounts` dict would look like this `{"K": 3, "Q": 1, "A": 1}`. So, we can determine whether a hand is a Three of a Kind type if there are three entries in the `cardCounts` dict and one of those entries has a value of `3`.

<h6>Is Two Pair</h6>

The fifth highest valued type of hand is two pairs. This means that 2 cards in a hand have the same value and another 2 cards are a pair. A `cardCounts` dict would look like this `{"K": 2, "Q": 2, "A": 1}`. So, we can determine whether a hand is a Two Pairs type if there are three entries in the `cardCounts` dict and one of those entries has a value of `2`. (The other three cards are split among the remaining 2 card values which means one of the other 2 card values has a count of 2)

<h6>Is One Pair</h6>

The sixth highest valued type of hand is one pairs. This means that 2 cards in a hand have the same value and the other cards are all unique. A `cardCounts` dict would look like this `{"K": 2, "Q": 1, "A": 1, "T": 1}`. So, we can determine whether a hand is a One Pair type if there are four entries in the `cardCounts` dict and one of those entries has a value of `2`.

<h6>High Card Case</h6>

The least valued type of hand is high card. This means that all 5 cards in a hand have unique values. A `cardCounts` dict would look like this `{"K": 1, "Q": 1, "A": 1, "T": 1, "9": 1}`. We could determine this if the `cardCounts` dict has five entries. However, we can also infer this if a hand has not previously been categorized in any of the more valued types.

<h4>Sorting the hands</h4>

I implemented an insertion sort algorithm that opperates similarly to JavaScripts, [Array.sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description) method.

The `compareCards()` function is analogous to js's `compareFn` parameter that returns `1` if the first hand should be place after the second hand, `0` if the first hand and second hand are exactly the same, or `-1` if the first hand should be place before the second hand. The return value is determined by first comparing the hands' types and if equal comparing the card values from left to right until one hand is determined to be a higher valued hand.

Another thing to note is the `getCardValue` function which takes a string card value (`2-9`, `T`, `J`, `Q`, `K`, or `A`) and returns a numeric value based on the face. It's pretty simple. For every possible string value, it returns a 2-digit int representing their value (`T => 10`, `J => 11`, `Q => 12`, `K => 13`, and `A => 14`). Otherwise, it casts the numeric string to an integer for the value.

One minor optimization I added here was that because every Five of a Kind is inherently more valuable that every Four of a Kind, and so on, we can create a unique list of hand for each hand type, so rather than having to iterate through every hand type, we only compare hands of similar types. This is done simply by creating a 2-dimentional list where the first index of the array corresponds to the hand type (`0-6`) and the second index refers to the sorted list of hands of that type.

<h4>Calculating the winnings</h4>

From here, we now have a sorted list of hands and all their bids. So, all we need to do is iterate through each hand, and sum the `hand.bid * rank` of each hand.

<h3>Part 2 (Jokers are wild)</h3>

The change to the challenge is simple. All the `J`s in the input file represent Jokers instead of Jacks. Jokers can be considered as any other card value in order to achieve the highest hand type possible. The trade off is that Joker cards are now the lowest card value (even lower than `2` cards).

As a result, there are only two considerable changes to the original code:

1. All Boolean Methods to Determine card type from the `cardCounts` dict are updated.
  - Previously, each of these could be generalize to have the exact same logic: "`cardCounts` has exacly `n` entries and one entry has value `m`."
  - Now, this logic is updated to "`cardCounts` has exacly `n` entries and one entry has value `m` OR (`cardCounts` has exacly `n + 1` entries and one entry has key `J` and any non-J entry `+ cardCounts["J"] == m`)."

2. The `getCardValue` method is updated so that `"J"` cards get a value of `1`.
