import * as S from './styles'

export type LineColors = 'primary' | 'secondary'

export type HeadingProps = {
  children: React.ReactNode
  color?: 'white' | 'black'
  lineLeft?: boolean
  lineBottom?: boolean
  lineColor?: LineColors
  size?: 'small' | 'medium'
}

const Heading = ({
  children,
  color = 'white',
  lineLeft = false,
  lineBottom = false,
  size = 'medium',
  lineColor = 'primary'
}: HeadingProps) => (
  <S.Wrapper
    size={size}
    color={color}
    lineBottom={lineBottom}
    lineColor={lineColor}
    lineLeft={lineLeft}
  >
    {children}
  </S.Wrapper>
)

export default Heading
