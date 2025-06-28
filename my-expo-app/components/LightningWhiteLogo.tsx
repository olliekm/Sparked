import * as React from "react";
import Svg, { G, Polygon, SvgProps } from "react-native-svg";
/* SVGR has dropped some elements not supported by react-native-svg: style */
const Lightning = (props: SvgProps) => (
  <Svg
    height={400}
    width={400}
    id="_x32_"
    xmlns="http://www.w3.org/2000/svg"
    xmlnsXlink="http://www.w3.org/1999/xlink"
    viewBox="0 0 512 512"
    xmlSpace="preserve"
    fill="#ffffff"
    stroke="#ffffff"
    {...props}
  >
    <G id="SVGRepo_bgCarrier" strokeWidth={0} />
    <G
      id="SVGRepo_tracerCarrier"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <G id="SVGRepo_iconCarrier">
      <G>
        <Polygon
          className="st0"
          points="386.415,193.208 287.481,193.208 359.434,0 161.566,0 125.585,280.151 206.528,280.151 170.557,512 "
        />
      </G>
    </G>
  </Svg>
);
export default Lightning;
