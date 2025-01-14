# Parking Lot

I own a parking lot that can hold upto 'n' vechiles at any given point in time. There are four entraces to the parking. I want to create an automated ticketing system that allows my customers to use my parking lot without human intervention.

When a vechile enters my parking lot, I want to have a ticket issued to the driver. The ticket issuing process includes us documenting the registration number (number plate) and the colour of the vechile and allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are nice enough to always park in the slots allocated to them). The customer should be allocated a parking slot which is nearest to their current entrance. At the exit the customer returns the ticket which then marks the slot they were using as being available. There are 3 types of parking spots, small, compact and large. Small vechiles can only park at small spots, etc.

Due to government regulation, the system should provide me with the ability to find out:

- Registration numbers of all vechiles of a particular colour.
- Slot number in which a vehicle with a given registration number is parked.
- Slot numbers of all slots where a vehicle of a particular colour is parked.

We interact with the system via a simple set of commands which produce a specific output. Please take a look at the example below, which includes all the commands you need to support - they're self explanatory. The system should allow input in two ways. Just to clarify, the same codebase should support both modes of input - we don't want two distinct submissions.

- It should provide us with an interactive command prompt based shell where commands can be typed in
- It should accept a filename as a parameter at the command prompt and read the commands from that file

