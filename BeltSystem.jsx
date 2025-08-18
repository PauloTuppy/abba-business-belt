import { useState } from 'react'
import { Badge } from '@/components/ui/badge.jsx'
import { Progress } from '@/components/ui/progress.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'

const BELT_LEVELS = [
  { 
    name: 'Branca', 
    color: 'bg-white border-gray-300 text-gray-800',
    bgColor: 'bg-gray-50',
    accentColor: 'text-gray-600',
    minPoints: 0,
    maxPoints: 100
  },
  { 
    name: 'Amarela', 
    color: 'bg-yellow-100 border-yellow-300 text-yellow-800',
    bgColor: 'bg-yellow-50',
    accentColor: 'text-yellow-600',
    minPoints: 100,
    maxPoints: 250
  },
  { 
    name: 'Laranja', 
    color: 'bg-orange-100 border-orange-300 text-orange-800',
    bgColor: 'bg-orange-50',
    accentColor: 'text-orange-600',
    minPoints: 250,
    maxPoints: 500
  },
  { 
    name: 'Verde', 
    color: 'bg-green-100 border-green-300 text-green-800',
    bgColor: 'bg-green-50',
    accentColor: 'text-green-600',
    minPoints: 500,
    maxPoints: 1000
  },
  { 
    name: 'Azul', 
    color: 'bg-blue-100 border-blue-300 text-blue-800',
    bgColor: 'bg-blue-50',
    accentColor: 'text-blue-600',
    minPoints: 1000,
    maxPoints: 2000
  },
  { 
    name: 'Roxa', 
    color: 'bg-purple-100 border-purple-300 text-purple-800',
    bgColor: 'bg-purple-50',
    accentColor: 'text-purple-600',
    minPoints: 2000,
    maxPoints: 4000
  },
  { 
    name: 'Marrom', 
    color: 'bg-amber-100 border-amber-600 text-amber-800',
    bgColor: 'bg-amber-50',
    accentColor: 'text-amber-700',
    minPoints: 4000,
    maxPoints: 8000
  },
  { 
    name: 'Preta', 
    color: 'bg-gray-900 border-gray-700 text-yellow-400',
    bgColor: 'bg-gray-900',
    accentColor: 'text-yellow-400',
    minPoints: 8000,
    maxPoints: Infinity
  }
]

export function BeltSystem({ userPoints = 45 }) {
  const currentBelt = BELT_LEVELS.find(belt => 
    userPoints >= belt.minPoints && userPoints < belt.maxPoints
  ) || BELT_LEVELS[0]
  
  const nextBelt = BELT_LEVELS[BELT_LEVELS.indexOf(currentBelt) + 1]
  
  const progressInCurrentBelt = nextBelt 
    ? ((userPoints - currentBelt.minPoints) / (nextBelt.minPoints - currentBelt.minPoints)) * 100
    : 100
  
  const pointsToNext = nextBelt ? nextBelt.minPoints - userPoints : 0

  return (
    <Card className={`${currentBelt.bgColor} border-2`}>
      <CardHeader className="pb-3">
        <CardTitle className="flex items-center justify-between">
          <span className={currentBelt.accentColor}>Faixa Atual</span>
          <Badge className={`${currentBelt.color} border-2`}>
            Faixa {currentBelt.name}
          </Badge>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span className={currentBelt.accentColor}>Progresso</span>
            <span className={currentBelt.accentColor}>
              {userPoints} / {nextBelt ? nextBelt.minPoints : '∞'} pontos
            </span>
          </div>
          <Progress 
            value={progressInCurrentBelt} 
            className="h-3"
          />
        </div>
        
        {nextBelt && (
          <div className="text-sm space-y-1">
            <p className={currentBelt.accentColor}>
              <strong>{pointsToNext} pontos</strong> para a próxima faixa
            </p>
            <p className="text-xs opacity-75">
              Próxima: Faixa {nextBelt.name}
            </p>
          </div>
        )}
        
        {!nextBelt && (
          <div className="text-sm">
            <p className={currentBelt.accentColor}>
              🏆 <strong>Parabéns!</strong> Você alcançou a faixa máxima!
            </p>
          </div>
        )}
      </CardContent>
    </Card>
  )
}

export function BeltIndicator({ userPoints = 45 }) {
  const currentBelt = BELT_LEVELS.find(belt => 
    userPoints >= belt.minPoints && userPoints < belt.maxPoints
  ) || BELT_LEVELS[0]

  return (
    <Badge className={`${currentBelt.color} border-2`}>
      Faixa {currentBelt.name}
    </Badge>
  )
}

export { BELT_LEVELS }

