from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here! 
class MoveActorsActon(Action):
  """An update action that moves all the actors
  The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
  than zero
  """
# Override the execute(cast, script) method as follows:
  def execute(self, cast, script):
    """Executes the move actors action
    
    Args:
      cast (Cast): Cast of actors in the game 
      script (Script): Script of actions in the game
    """
# 1) get all the actors from the cast
    actors = cast.get_all_actors()
# 2) loop through the actors
    for actor in actors:
# 3) call the move_next() method on each actor
      actor.move_next()