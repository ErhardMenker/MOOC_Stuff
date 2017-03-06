"""
90% !!!
"""

"""
Cookie Clicker Simulator
"""

import simpleplot

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
import math

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._produced = 0.0
        self._inventory = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._hist = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        output = "time: " + str(self._time) + " produced: " + str(self._produced) + " available: " + str(self._inventory) + " CPS: " + str(self._cps)
        return output
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._inventory
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._hist

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self.get_cookies() - cookies >= 0:
            return 0.0
        else:
            return math.ceil((cookies - self.get_cookies()) / self.get_cps())
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """

        if time <= 0.0:
            return None
        else:
            self._produced += (self.get_cps() * time)
            self._inventory += (self.get_cps() * time)
            self._time += time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        cost = float(cost)
        if cost > self._inventory:
            return None
        else:
            self._inventory -= cost
            self._cps += additional_cps
            #archive the circumstances around this purchase
            archive = (self._time, item_name, cost, self._produced)
            self._hist.append(archive)
            

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    
    build_info_clone = build_info.clone()
    this_state = ClickerState()
        
    while True:

        #exit simulation if out of time or strategy does not return any item to be bought or an item could not be bought before game ends
        item = strategy(this_state.get_cookies(), this_state.get_cps(), this_state.get_history(), duration - this_state.get_time(), build_info_clone)
        if this_state.get_time() > duration: 
            break
        elif item == None or this_state.time_until(build_info_clone.get_cost(item)) > (duration - this_state.get_time()):
            this_state.wait(duration - this_state.get_time())
            break
        else:
            this_state.wait(this_state.time_until(build_info_clone.get_cost(item)))
            this_state.buy_item(item, build_info_clone.get_cost(item), build_info_clone.get_cps(item))
            build_info_clone.update_item(item)

    return this_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cheapest = float("inf")
    cheapest_option = None
    build_options = build_info.build_items()
    for build_option in build_options:
        build_cost = build_info.get_cost(build_option)
        if (cheapest > build_cost) and (build_cost <= (cookies + cps * time_left)):
            cheapest = build_cost
            cheapest_option = build_option
    return cheapest_option


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    priciest = float("-inf")
    priciest_option = None
    build_options = build_info.build_items()
    for build_option in build_options:
        build_cost = build_info.get_cost(build_option)
        if (priciest < build_cost) and (build_cost <= (cookies + cps * time_left)):
            priciest = build_cost
            priciest_option = build_option
    return priciest_option

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    I will upgrade later, this just picks most expensive.
    """
    priciest = float("-inf")
    priciest_option = None
    build_options = build_info.build_items()
    for build_option in build_options:
        build_cost = build_info.get_cost(build_option)
        if (priciest < build_cost) and (build_cost <= (cookies + cps * time_left)):
            priciest = build_cost
            priciest_option = build_option
    return priciest_option
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
    